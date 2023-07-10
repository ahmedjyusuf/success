import React, { useEffect, useState } from 'react';
import axios from 'axios';
import {Link} from 'react-router-dom'

const Profile = () => {
  const [zoom, setZoom] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem('access');

    // Function to set the token in the request headers
    const setAuthToken = token => {
      if (token) {
        axios.defaults.headers.common['Authorization'] = `JWT ${token}`;
      } else {
        delete axios.defaults.headers.common['Authorization'];
      }
    };

    // Call setAuthToken with the token
    setAuthToken(token);

    // Make API requests to the Django backend
    // Example: Retrieve data from an endpoint '/api/data'
    axios
      .get(`${process.env.REACT_APP_API_URL}/zoom/local-class/`)
      .then(response => {
        // Handle the response data
        console.log(response.data);
        setZoom(response.data);
      })
      .catch(error => {
        // Handle the error
        console.error(error);
      });
  }, []);
  const formatDate = (datestr) => {
    const date = new Date(datestr);
    const formatedTime = date.toLocaleString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
    // const amPm = hour.slice(-2);
    return formatedTime
  }
  return (
    <div>
      <h1>User Profile</h1>
      <h2>Zoom Class Details:</h2>
      {zoom.length > 0 ? (
        <ul>
          {zoom.map((zoomclass, index) => (
            <li key={index}>
              <h3>Class - {zoomclass.zoom_class.name}</h3>
              <ul>
                <li>Teacher: {zoomclass.zoom_class.teacher}</li>
                
                <li>Days: {zoomclass.days_of_week.join(', ')}</li>
                <li>Time: {formatDate(zoomclass.class_time)}</li>
                <li>Link: <Link to={zoomclass.zoom_class.link}>{zoomclass.zoom_class.link}</Link></li>
                
              </ul>
            </li>
          ))}
        </ul>
      ) : (
        <p>Loading Zoom class details...</p>
      )}
    </div>
  );
};

export default Profile;