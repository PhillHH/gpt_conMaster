import React from 'react';
import './InfoCard.css';

function InfoCard({ title, text, image, alt, linkText, linkHref }) {
    return (
        <div className="info-card">
            {image && <img src={image} alt={alt} className="card-image" />}
            <div className="card-content">
                <h3 className="card-title">{title}</h3>
                <p className="card-text">{text}</p>
                {linkText && linkHref && (
                    <a href={linkHref} className="card-link">
                        {linkText}
                    </a>
                )}
            </div>
        </div>
    );
}

export default InfoCard;
