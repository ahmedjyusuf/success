import React, {useState} from 'react'
import {Link, useNavigate, Route, redirect, useParams} from 'react-router-dom'
import {connect} from 'react-redux'
import { reset_password_confirm } from '../actions/auth'


import Home from './Home'

const ResetPasswordConfirm = ({ match ,reset_password_confirm }) => {
    const [requestSent, setrequestSent] = useState(false)
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        new_password: '',
        re_new_password: '' 
    });

    const { uid, token } = useParams();
    const { new_password, re_new_password } = formData;

    const onChange = e => {
        setFormData({ ...formData, [e.target.name]: e.target.value })
        console.log({ ...formData, [e.target.name]: e.target.value })
    };

    const onSubmit = e => {
        e.preventDefault();
        
        // const uid = match.params.uid
        // const token = match.params.token
      
        reset_password_confirm(uid, token, new_password, re_new_password);
        setrequestSent(true)
        console.log(uid, token, new_password, re_new_password,'\n\n\n')
    };

    // if auth then redirect to 
    if (requestSent){
        navigate('/');
        return null;
    }
  return (
    <div className='container mt-5'>
        <form onSubmit={e => onSubmit(e)}>
            <div className='form-group'>
                <input
                    className='form-control'
                    type='password'
                    placeholder='New Password'
                    name='new_password'
                    value={new_password}
                    autocomplete="off"
                    onChange={e => onChange(e)}
                    minLength='4'
                    require
                />
            </div>
            <div className='form-group'>
                <input
                    className='form-control'
                    type='password'
                    placeholder='Confirm New Password'
                    name='re_new_password'
                    value={re_new_password}
                    autocomplete="off"
                    onChange={e => onChange(e)}
                    minLength='4'
                    require
                />
            </div>
            <button className='btn btn-primary' type='submit'>Reset Password</button>
        </form>
    </div>
  )
}

// const mapStateToProps = state => ({
//     // is authenticated
// });

export default connect(null, { reset_password_confirm })(ResetPasswordConfirm)

