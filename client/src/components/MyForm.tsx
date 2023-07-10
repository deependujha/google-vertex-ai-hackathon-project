'use client';
import React, { useState } from 'react';
import axios from 'axios';
import { errorAlert } from '@/utils/SweetAlert';
import MyLoadingModal from './MyLoadingModal';

const defaultForm = {
	businessName: '',
	businessEmail: '',
	businessDescription: '',
};

const MyForm = () => {
	const [form, setForm] = useState(defaultForm);

	function toggleModal() {
		const body = document.querySelector('body');
		const modal = document.querySelector('.modal');
		// Check if 'opacity-0' class is present on modal
		// @ts-ignore
		const isOpacityZero = modal.classList.contains('opacity-0');

		// Check if 'pointer-events-none' class is present on modal
		// @ts-ignore
		const isPointerEventsNone = modal.classList.contains('pointer-events-none');

		// Check if 'modal-active' class is present on body
		// @ts-ignore
		const isModalActive = body.classList.contains('modal-active');

		// @ts-ignore
		modal.classList.toggle('opacity-0');
		// @ts-ignore
		modal.classList.toggle('pointer-events-none');
		// @ts-ignore
		body.classList.toggle('modal-active');
	}

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
		console.log('clicked on button');
		try {
			toggleModal();
			console.log('going to make request');
			const response = await axios({
				method: 'post',
				url: 'http://13.233.138.109/create-website',
				data: { ...form },
				responseType: 'blob',
			});

			console.log('request successfull');

			// console.log('response: ', response.data);
			// Create blob link to download
			const href = URL.createObjectURL(response.data);

			// create "a" HTML element with href to file & click
			const link = document.createElement('a');
			link.href = href;
			toggleModal();

			link.setAttribute('download', `${form.businessName}-website.zip`); //or any other extension
			document.body.appendChild(link);
			link.click();

			// clean up "a" element & remove ObjectURL
			document.body.removeChild(link);
			URL.revokeObjectURL(href);

			setForm(defaultForm);
		} catch {
			toggleModal();
			errorAlert();
			console.log('error occurred');
		}
		console.log('everything over');
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
			<MyLoadingModal toggleModal={toggleModal} />
		</div>
	);
};

export default MyForm;
