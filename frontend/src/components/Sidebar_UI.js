import React, { useState } from 'react';
import './sidebarUI.css';

// Importiere die beiden Logos
import fullLogo from '../assets/logo_full.png'; // Vollständiges Logo
import iconLogo from '../assets/logo_icon.png'; // Nur das Icon

function Sidebar_UI() {
    const [isCollapsed, setIsCollapsed] = useState(false); // Standardmäßig auf "false" gesetzt

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
                    <a href="/overview" className="menu-item">
                        <i className="icon-overview"></i>
                        {!isCollapsed && <span>Overview</span>}
                    </a>
                </li>
                <li>
                    <a href="/news" className="menu-item">
                        <i className="icon-news"></i>
                        {!isCollapsed && <span>&nbsp;&nbsp;&nbsp;News</span>}
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
                        {!isCollapsed && <span>&nbsp;Functions</span>}
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