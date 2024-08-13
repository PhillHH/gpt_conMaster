import React from 'react';
import AdvancedSidebar from './components/Sidebar_UI';
import Overview from './pages/Overview';

function App() {
    return (
        <div className="App">
            <AdvancedSidebar />
            <div className="content">
                <Overview />
                {/* Weitere Seiten können hier hinzugefügt werden */}
            </div>
        </div>
    );
}

export default App;
