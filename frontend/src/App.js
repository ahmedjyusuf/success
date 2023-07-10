import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import {Provider} from 'react-redux'
import store from './store';

import Layout from './hocs/Layout';
import Home from "./container/Home";
import Login from "./container/Login";
import Signup from "./container/Signup";
import Activate from "./container/Activate";
import ResetPassword from "./container/ResetPassword";
import ResetPasswordConfirm from "./container/ResetPasswordConfirm";
import Users from './container/Users';
import Profile from './container/Profile';
// 
function App() {
  return (
    <Provider store={store}>
      <Router>
        <Layout>
          <Routes>
            <Route exact path='/' Component={Home} />
            <Route exact path='/login' Component={Login} />
            <Route exact path='/signup' Component={Signup} />
            <Route exact path='/profile' Component={Profile} />
            <Route exact path='/api/users/' Component={Users} />
            <Route exact path='/reset-password' Component={ResetPassword} />
            <Route exact path='/password/reset/confirm/:uid/:token' Component={ResetPasswordConfirm} />
            <Route exact path='/activate/:uid/:token' Component={Activate} />
          </Routes>
        </Layout>
      </Router>
    </Provider>
    
  );
}

export default App;
