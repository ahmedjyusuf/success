import React, {useState} from 'react'
import {Link, useNavigate, Route, redirect, useParams} from 'react-router-dom'
import {connect} from 'react-redux'
import { verify } from '../actions/auth'


import Home from './Home'

const Activate = ({ match ,verify }) => {
    const [verified, setVerified] = useState(false)
    const navigate = useNavigate();


    const { uid, token } = useParams();


    const verifyAccount = e => {
        e.preventDefault();
        verify(uid, token);
        setVerified(true)
    };

    // if auth then redirect to 
    if (verified){
        navigate('/');
        return null;
    }
  return (
    <div className='container'>
      <div 
          className='d-flex flex-column justify-content-center align-items-center'
          style={{ marginTop: '200px' }}
      >
          <h1>Verify your Account:</h1>
          <button
              onClick={verifyAccount}
              style={{ marginTop: '50px' }}
              type='button'
              className='btn btn-primary'
          >
              Verify
          </button>
      </div>
  </div>
  )
}

export default connect(null, { verify })(Activate)
