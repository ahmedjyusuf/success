import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { checkAuthenticated, logout } from '../actions/auth';

const Home = () => {
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated);
  const user = useSelector(state => state.auth.user);
  const dispatch = useDispatch();

  useEffect(() => {
    dispatch(checkAuthenticated());
  }, [dispatch]);

  const handleLogout = () => {
    dispatch(logout());
  };

  if (isAuthenticated) {
    return (
      <div>
        <h1>Welcome, {user && user.first_name}!</h1>
        <button onClick={handleLogout}>Logout</button>
      </div>
    );
  } else {
    return <h1>
      Hi, Please login to
    </h1>;
  }
};

export default Home;
