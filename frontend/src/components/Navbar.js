import React, {Fragment} from 'react'
import { Link } from 'react-router-dom'
import { connect } from 'react-redux'
import {logout } from '../actions/auth'


const Navbar = ({ logout, isAuthenticated }) => {
  const guestLink = () => (
    <Fragment>
        <li className="nav-item">
            <Link className="nav-link" to="/login">Login</Link>
          </li>
          <li className="nav-item">
            <Link className="nav-link" to="/signup">Sign Up</Link>
        </li>
    </Fragment>
  )
  const authLinks = () => (
    <Fragment>
    <Link className="nav-link" to="/profile">Profile</Link>
    <a className="nav-link" href="#!" onClick={logout}>Logout</a>
    </Fragment>
  )

  return (
    <div>
      <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <Link className="navbar-brand" href="/">Meta Tutoring</Link>
        <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNav">
          <ul className="navbar-nav">
            <li className="nav-item active">
              <Link className="nav-link" to="/">Home <span className="sr-only"></span></Link>
            </li>
            {isAuthenticated ? authLinks() : guestLink()}
          </ul>
        </div>
      </nav>
    </div>
  )
}
const mapStatetoProps = state => ({
  isAuthenticated: state.auth.isAuthenticated
})
export default connect(mapStatetoProps, {logout})(Navbar)
