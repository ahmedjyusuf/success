import React, {useState} from 'react'
import {Link, useNavigate, Route, redirect} from 'react-router-dom'
import {connect} from 'react-redux'
import {signup} from '../actions/auth'
import Home from './Home'

const Signup = ({ signup, isAuthenticated, error }) => {
  const [accountCreated, setAccountCreated] = useState(false);
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      re_password: ''
  });


  const { first_name, last_name, email, password, re_password } = formData;

  const onChange = e => {
      setFormData({ ...formData, [e.target.name]: e.target.value })
      console.log({ ...formData, [e.target.name]: e.target.value })
  };

  const onSubmit = e => {
      
      e.preventDefault();

      if (password === re_password) {
        signup(first_name, last_name, email, password, re_password);
        console.log('the info before submttting', first_name, last_name, email, password, re_password)
        // setAccountCreated(true);
    }
    console.log('server_erros', error)
  };

  // if auth then redirect to 
  if (isAuthenticated){
      navigate('/');
      return null;
  }
  if (accountCreated) {
    navigate('/');
    return null
  }
  
  return (
    <div className='container mt-5'>
        <h1>Sign Up</h1>
        <p>Create your Account</p>
        <form onSubmit={e => onSubmit(e)}>
        <div className='form-group'>
          <input
            className='form-control'
            type='text'
            placeholder='First Name*'
            name='first_name'
            value={first_name}
            onChange={e => onChange(e)}
            required
          />
          </div>
          <div className='form-group'>
              <input
                  className='form-control'
                  type='text'
                  placeholder='Last Name*'
                  name='last_name'
                  value={last_name}
                  onChange={e => onChange(e)}
                  required
              />
          </div>
          <div className='form-group'>
              <input
                  className='form-control'
                  type='email'
                  placeholder='Email*'
                  name='email'
                  value={email}
                  onChange={e => onChange(e)}
                  required
              />
          </div>
          <div className='form-group'>
              <input
                  className='form-control'
                  type='password'
                  placeholder='Password*'
                  name='password'
                  value={password}
                  onChange={e => onChange(e)}
                  minLength='4'
                  required
              />
          </div>
          <div className='form-group'>
              <input
                  className='form-control'
                  type='password'
                  placeholder='Confirm Password*'
                  name='re_password'
                  value={re_password}
                  onChange={e => onChange(e)}
                  minLength='6'
                  required
              />
          </div>
          {error && <p className='text-danger'>{error}</p>}
            <button className='btn btn-primary' type='submit'>Sign up</button>
        </form>
        <p className='mt-3'>
            Already have an account? <Link to='/login'>Sign up</Link>
        </p>
    </div>
  )
}

// const mapStateToProps = state => ({
//     // is authenticated
// });
const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated,
    error: state.auth.error
});
export default connect(mapStateToProps, { signup })(Signup)
