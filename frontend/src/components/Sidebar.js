import React from 'react';

function Sidebar({ isOpen, toggleSidebar }) {
  return (
    <div className={`sidebar ${isOpen ? 'open' : ''}`}>
      <button onClick={toggleSidebar}>
        {isOpen ? 'Close Menu' : 'Open Menu'}
      </button>
      <nav>
        <ul>
          <li><a href="/overview">Overview</a></li>
          <li><a href="/news">News</a></li>
          <li><a href="/chat">Conversions</a></li>
          <li><a href="/chat">Functions</a></li>
        </ul>
      </nav>
    </div>
  );
}

export default Sidebar;