import React, { useState } from 'react';
import './sidebarUI.css';

import fullLogo from '../assets/logo_full.png';
import iconLogo from '../assets/logo_icon.png';

function Sidebar_UI() {
    const [isCollapsed, setIsCollapsed] = useState(false);

    const toggleSidebar = () => {
        setIsCollapsed(!isCollapsed);
    };

    return (
        <div className={`sidebar ${isCollapsed ? 'collapsed' : ''}`}>
            <div className="logo">
                <img src={isCollapsed ? iconLogo : fullLogo} alt="Logo" />
            </div>
            <ul className="menu">
                <li>
                    <a href="overview" className="menu-item">
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
                    <a href="/chats" className="menu-item">
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
