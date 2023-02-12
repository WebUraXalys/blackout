export const initialValues = {
    firstName: {
        value: '',
        error: '',
        required: true,
        validate: 'text',
        minLength: 2,
        maxLength: 20,
        helperText: 'Custom error message'
    },
    lastName: {
        value: '',
        error: '',
        required: true,
        validate: 'text',
        minLength: 2,
        maxLength: 20
    },
    email: {
        value: '',
        error: '',
        validate: 'email'
    },
    gender: {
        value: '',
        error: '',
        validate: 'select'
    },
    city: {
        value: '',
        error: '',
        validate: 'text',
        minLength: 3,
        required: true,
        maxLength: 15
    },
    street: {
        value: '',
        error: '',
        validate: 'text',
        minLength: 3,
        required: true,
        maxLength: 20
    },
    number: {
        value: '',
        error: '',
        minLength: 1,
        required: true,
        maxLength: 5
    },
    agreement: {
        value: false,
        error: '',
        required: true,
        validate: 'checkbox',
        helperText: 'Please accept our terms and conditions'
    },
    phone: {
        value: '',
        error: '',
        validate: 'phone',
        maxLength: 15
    }
};