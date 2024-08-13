import React, { useState } from 'react';
import './sidebarUI.css';

import logo from '../assets/logo_full.png';


function Sidebar_UI() {
    const [isCollapsed, setIsCollapsed] = useState(true);

    const toggleSidebar = () => {
        setIsCollapsed(!isCollapsed);
    };

    return (
        <div className={`sidebar ${isCollapsed ? 'collapsed' : ''}`}>
            <div className="logo">
                <img src={logo} alt="Logo" />
            </div>
            <ul className="menu">
                <li>
                    <a href="/overview" className="menu-item">
                        <i className="icon-overview"></i>
                        {!isCollapsed && <span>Overview</span>}
                    </a>
                </li>
                <li>
                    <a href="/news" className="menu-item">
                        <i className="icon-news"></i>
                        {!isCollapsed && <span>News</span>}
                    </a>
                </li>
                <li>
                    <a href="/conversations" className="menu-item">
                        <i className="icon-conversations"></i>
                        {!isCollapsed && <span>Conversations</span>}
                    </a>
                </li>
                <li>
                    <a href="/functions" className="menu-item">
                        <i className="icon-functions"></i>
                        {!isCollapsed && <span>Functions</span>}
                    </a>
                </li>
            </ul>
            <div className="toggle-btn" onClick={toggleSidebar}>
                <i className="icon-toggle"></i>
            </div>
        </div>
    );
}

export default Sidebar_UI;
