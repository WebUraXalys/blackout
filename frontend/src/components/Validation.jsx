import React from 'react';

const Validation = (values) => {
    let errors = {};

    errors.city = !values.city;
    errors.street = !values.street;
    errors.number = !values.number;

    return errors;
};

export default Validation;