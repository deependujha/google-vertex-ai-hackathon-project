'use client';
import React, { useState } from 'react';
import axios from 'axios';
import { errorAlert } from '@/utils/SweetAlert';

const defaultForm = {
	businessName: '',
	businessEmail: '',
	businessDescription: '',
};

const MyForm = () => {
	const [form, setForm] = useState(defaultForm);

	const onInputChange = (
		e:
			| React.ChangeEvent<HTMLInputElement>
			| React.ChangeEvent<HTMLTextAreaElement>
	) => {
		const { name, value } = e.target;
		setForm({ ...form, [name]: value });
	};

	const onBtnClick = async () => {
		// console.log(form);
		const response = await axios({
			method: 'post',
			url: 'http://127.0.0.1:8080/create-website',
			data: { ...form },
			responseType: 'blob',
		});

		// console.log('response: ', response.data);
		// Create blob link to download
		const href = URL.createObjectURL(response.data);

		// create "a" HTML element with href to file & click
		const link = document.createElement('a');
		link.href = href;
		link.setAttribute('download', 'myZipFile.zip'); //or any other extension
		document.body.appendChild(link);
		link.click();

		// clean up "a" element & remove ObjectURL
		document.body.removeChild(link);
		URL.revokeObjectURL(href);

		setForm(defaultForm);
		// errorAlert();
	};
	return (
		<div
			className="bg-gradient-to-r from-white to-purple-500 flex justify-center items-center"
			style={{ height: '100vh' }}
		>
			<div>
				<div className="text-center text-lg overflow-hidden pb-5">
					Just fill the form below, and get your website ready in 2 minutes. 🧑‍💻
				</div>
				<div
					className="container bg-white rounded-xl px-5 py-5"
					style={{ width: '600px', border: '1px solid black' }}
				>
					<div className="mb-4">
						<label
							className="block text-gray-700 text-sm font-bold mb-2"
							htmlFor="businessName"
						>
							Business Name
						</label>
						<input
							className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
							id="businessName"
							name="businessName"
							type="text"
							placeholder="myBusiness"
							value={form.businessName}
							onChange={onInputChange}
						/>
					</div>
					<div className="mb-4">
						<label
							className="block text-gray-700 text-sm font-bold mb-2"
							htmlFor="businessEmail"
						>
							Business email
						</label>
						<input
							className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
							id="businessEmail"
							name="businessEmail"
							type="email"
							placeholder="myBusiness@gmail.com"
							value={form.businessEmail}
							onChange={onInputChange}
						/>
					</div>
					<div className="mb-4">
						<label
							className="block text-gray-700 text-sm font-bold mb-2"
							htmlFor="businessDescription"
						>
							Description
						</label>
						<textarea
							value={form.businessDescription}
							className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline resize-none"
							id="businessDescription"
							name="businessDescription"
							placeholder="Describe your business"
							rows={6}
							onChange={onInputChange}
						/>
					</div>

					<div className="flex justify-center">
						<button
							className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
							type="button"
							style={{ width: '100%' }}
							onClick={onBtnClick}
						>
							Create website
						</button>
					</div>
				</div>
			</div>
		</div>
	);
};

export default MyForm;