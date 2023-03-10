import React, { useState } from 'react';

function Home() {
const [showModal, setShowModal] = useState(false);
const [firstName, setFirstName] = useState('');
const [lastName, setLastName] = useState('');
const [email, setEmail] = useState('');

const handleConfirm = () => {
	// create a new component with the input data
	const newComponent = <NewComponent firstName={firstName} lastName={lastName} email={email} />;
	// do something with the new component
	console.log(newComponent);
	// close the modal
	setShowModal(false);
}

return (
	<div>
		<button onClick={() => setShowModal(true)}>Open Modal</button>
		{showModal && (
			<div className="modal">
				<div className="modal-content">
					<h2>Enter your information</h2>
					<label htmlFor="first-name">First Name:</label>
					<input type="text" id="first-name" value={firstName} onChange={(e) => setFirstName(e.target.value)} />
					<label htmlFor="last-name">Last Name:</label>
					<input type="text" id="last-name" value={lastName} onChange={(e) => setLastName(e.target.value)} />
					<label htmlFor="email">Email:</label>
					<input type="email" id="email" value={email} onChange={(e) => setEmail(e.target.value)} />
					<div className="button-group">
						<button onClick={() => setShowModal(false)}>Cancel</button>
						<button onClick={handleConfirm}>Confirm</button>
					</div>
				</div>
			</div>
		)}
	</div>
);
}

function NewComponent({ firstName, lastName, email }) {
	return (
		<div>
			<h2>New Component</h2>
			<p>First Name: {firstName}</p>
			<p>Last Name: {lastName}</p>
			<p>Email: {email}</p>
		</div>
	);
}

export default Home;