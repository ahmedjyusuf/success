import React, {useState} from 'react'
import {Link, useNavigate, Route, redirect} from 'react-router-dom'
import {connect} from 'react-redux'
import { reset_password } from '../actions/auth'
import Home from './Home'

const ResetPassword = ({ reset_password }) => {
    const [requestSent, setrequestSent] = useState(false)
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        email: '',
    });


    const { email } = formData;

    const onChange = e => {
        setFormData({ ...formData, [e.target.name]: e.target.value })
        console.log({ ...formData, [e.target.name]: e.target.value })
    };

    const onSubmit = e => {
        console.log('formdata',formData)
        e.preventDefault();

        reset_password(email);
        setrequestSent(true)
    };

    // if auth then redirect to 
    if (requestSent){
        navigate('/');
        return null;
    }
  return (
    <div className='container mt-5'>
        <h1>Reset password</h1>

        <form onSubmit={e => onSubmit(e)}>
            <div className='form-group'>
                <input
                    className='form-control'
                    type='email'
                    placeholder='Email'
                    name='email'
                    value={email}
                    onChange={e => onChange(e)}
                    require
                />
            </div>
            <button className='btn btn-primary' type='submit'>Login</button>
        </form>
    </div>
  )
}

export default connect(null, { reset_password })(ResetPassword)
