export const initialValues = {
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
    // title: {
    //     value: '',
    //     error: '',
    //     minLength: 1,
    //     validate: 'text',
    //     required: true,
    //     maxLength: 10
    // },
    // icon: {
    //     value: null,
    //     error: '',
    //     required: true
    // }
    // agreement: {
    //     value: false,
    //     error: '',
    //     required: true,
    //     validate: 'checkbox',
    //     helperText: 'Please accept our terms and conditions'
    // },
};