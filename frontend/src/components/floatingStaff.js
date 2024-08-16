import React from 'react';
import './floatingStaff.css';

function floatingStaff() {
  return (
    <div className="container">
      <div className="avatar">
        <a href="https://codepen.io/">
          <img src="https://media.licdn.com/dms/image/v2/D4D03AQEUzhekiXiyJA/profile-displayphoto-shrink_200_200/profile-displayphoto-shrink_200_200/0/1720524378101?e=1729123200&v=beta&t=Z1aPsb_pZ_YoX7gnE88dnGX5QfZqyb2Hf759TsNjr3g" alt="Skytsunami" />
        </a>
      </div>
      <div className="content">
        <h1>Phillip Rugullis</h1>
        <p>Developer</p>
        <p>
          <span><a href="https://twitter.com/" target="_blank" rel="noopener noreferrer"><i className="fa fa-twitter"></i></a></span>
          <span><a href="https://github.com/" target="_blank" rel="noopener noreferrer"><i className="fa fa-github"></i></a></span>
          <span><a href="https://bitbucket.org/" target="_blank" rel="noopener noreferrer"><i className="fa fa-bitbucket"></i></a></span>
          <span><a href="https://codepen.io/" target="_blank" rel="noopener noreferrer"><i className="fa fa-codepen"></i></a></span>
        </p>
        <p>BY: Phillip Rugullis</p>
      </div>
    </div>
  );
}

export default floatingStaff;
