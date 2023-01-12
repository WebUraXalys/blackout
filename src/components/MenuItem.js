import React from 'react';

const MenuItem = (props) => {
    return (
        <a href="#" className="menu-item">
            <img src={props.item.img} alt=""/>
            <span>{props.item.title}</span>
        </a>
    );
};

export default MenuItem;