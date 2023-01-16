import React from 'react';

const MenuItem = (props) => {
    return (
        <div className="menu_el">
            <img className="svg_menu" src={props.item.img} alt="picture"/>
            <p className="menu_text">{props.item.title}</p>
        </div>
    );
};

export default MenuItem;