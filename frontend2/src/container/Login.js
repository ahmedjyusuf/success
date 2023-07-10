import React, {useState} from 'react'
import {Link, useNavigate, Route, redirect} from 'react-router-dom'
import {connect} from 'react-redux'
import {login} from '../actions/auth'
import Home from './Home'

const Login = ({ login, isAuthenticated }) => {
    const navigate = useNavigate();
    const [formData, setFormData] = useState({
        email: '',
        password: '' 
    });


    const { email, password } = formData;

    const onChange = e => {
        setFormData({ ...formData, [e.target.name]: e.target.value })
        console.log({ ...formData, [e.target.name]: e.target.value })
    };

    const onSubmit = e => {
        console.log('formdata',formData, email)
        e.preventDefault();

        login(email, password);
    };

    // if auth then redirect to 
    if (isAuthenticated){
        navigate('/');
    }
  return (
    <div className='container mt-5'>
        <h1>Sign In</h1>
        <p>Sign in to your Account</p>
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
            <div className='form-group'>
                <input
                    className='form-control'
                    type='password'
                    placeholder='Password'
                    name='password'
                    value={password}
                    autocomplete="off"
                    onChange={e => onChange(e)}
                    minLength='4'
                    require
                />
            </div>
            <button className='btn btn-primary' type='submit'>Login</button>
        </form>
        <p className='mt-3'>
            Don't have an account? <Link to='/signup'>Sign up</Link>
        </p>
        <p className='mt-3'>
            Forgot your Password? <Link to='/reset-password'>Reset Password</Link>
        </p>
    </div>
  )
}

// const mapStateToProps = state => ({
//     // is authenticated
// });
const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});
export default connect(mapStateToProps, { login })(Login)