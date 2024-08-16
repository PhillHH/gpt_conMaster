import React from 'react';
import './floatingStaff.css';

function FloatingStaff() {
  return (
    <div className="horizontal-layout">
      <div className="container">
        <div className="avatar">
          <a href="https://www.linkedin.com/in/phillipdot/">
            <img src="https://media.licdn.com/dms/image/v2/D4D03AQEUzhekiXiyJA/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1720524378111?e=1729123200&v=beta&t=tcJENqYzq6zSgeGleTVqrsuMvfImsvx8Hf1fQ9DrOvI" alt="Phillip Rugullis" />
          </a>
        </div>
        <div className="content">
          <h1>Phillip Rugullis</h1>
          <p>Developer</p>
          <p><a href="https://www.linkedin.com/in/phillipdot/">https://www.linkedin.com/in/phillipdot/</a></p>
        </div>
      </div>

      <div className="container">
        <div className="avatar">
          <a href="https://www.linkedin.com/in/georgi-slavov/">
            <img src="https://media.licdn.com/dms/image/D4E03AQHrbA3hT6UlLA/profile-displayphoto-shrink_800_800/0/1723686486084?e=1729123200&v=beta&t=cn7SlNtSPjT4Y1e2fiXZIEXxYKPN97aL90tPGfbAGiE" alt="Georgi Slavov" />
          </a>
        </div>
        <div className="content">
          <h1>Georgi Slavov</h1>
          <p>Graphic & UX Designer</p>
          <p><a href="https://www.linkedin.com/in/georgi-slavov/">https://www.linkedin.com/in/georgi-slavov/</a></p>
        </div>
      </div>
    </div>
  );
}

export default FloatingStaff;