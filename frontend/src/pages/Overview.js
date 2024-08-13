import React from 'react';
import ContentBox from '../components/ContentBox'; // Stellen Sie sicher, dass der Import korrekt ist

function Overview() {
  return (
    <ContentBox>
      <div className="overview">
        <h1>Overview</h1>
        <p>This will be a huge project soon. Make things happen with Growento.com:</p>
        {/* Hier kannst du eine Liste der letzten Aktivitäten hinzufügen */}
      </div>
    </ContentBox>
  );
}

export default Overview;