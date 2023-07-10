import requests
import uuid
import time

def evc(merchantUId, 
        apiUserId,apiKey, 
        customerMobileNumber, 
        description, amount, 
        autoWithdraw, merchantNo
        ):

        def responseMsg(status, message):
            return {'status': status, 'message': message}

        if not merchantUId:
            return responseMsg(400, 'Merchant user id is required')
        if not apiUserId:
            return responseMsg(400, 'API user id is required')
        if not apiKey:
            return responseMsg(400, 'API key is required')
        if not customerMobileNumber:
            return responseMsg(400, 'Customer mobile number is required')
        if not description:
            return (400, 'Description is required')
        if not amount:
            return (400, 'Amount is required')
        if len(str(customerMobileNumber)) != 12:
            return (400, 'Customer mobile number must be 12 digits')

        if autoWithdraw:
            if len(str(merchantNo)) != 9:
                return (400, 'Merchant number must be 9 digits')

        paymentObject = {
            'schemaVersion': '1.0',
            'requestId': str(uuid.uuid4()),
            'timestamp': int(time.time() * 1000),
            'channelName': 'WEB',
            'serviceName': 'API_PURCHASE',
            'serviceParams': {
                'merchantUid': merchantUId,
                'apiUserId': apiUserId,
                'apiKey': apiKey,
                'paymentMethod': 'MWALLET_ACCOUNT',
                'payerInfo': {
                    'accountNo': customerMobileNumber,
                },
                'transactionInfo': {
                    'referenceId': str(uuid.uuid4()),
                    'invoiceId': f"{str(uuid.uuid4())[:5]}-{customerMobileNumber}",
                    'amount': float(amount),
                    'currency': 'USD',
                    'description': description,
                },
            },
        }

        netAmount = float(amount) * 0.01

        withdrawalObject = {
            'schemaVersion': '1.0',
            'requestId': str(uuid.uuid4()),
            'timestamp': int(time.time() * 1000),
            'channelName': 'WEB',
            'serviceName': 'API_CREDITACCOUNT',
            'serviceParams': {
                'merchantUid': merchantUId,
                'apiUserId': apiUserId,
                'apiKey': apiKey,
                'paymentMethod': 'MWALLET_ACCOUNT',
                'payerInfo': {
                    'accountNo': merchantNo,
                    'accountType': 'MERCHANT',
                },
                'transactionInfo': {
                    'referenceId': str(uuid.uuid4()),
                    'invoiceId': f"{str(uuid.uuid4())[:5]}-{merchantNo}",
                    'amount': float(amount) - netAmount,
                    'currency': 'USD',
                    'description': description,
                },
            },
        }

        response = requests.post('https://api.waafipay.net/asm', json=paymentObject)
        data = response.json()

        # 5206 => payment has been canceled
        # 2001 => payment has been done successfully
        if int(data.get('responseCode', 0)) == 2001:
            print('success')
        else:
            print('failed')