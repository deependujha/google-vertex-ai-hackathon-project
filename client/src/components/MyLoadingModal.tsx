'use client';
import React, { useState } from 'react';

type Prop = {
	toggleModal: () => void;
};

function MyLoadingModal({ toggleModal }: Prop) {
	return (
		<div className="modal opacity-0 pointer-events-none fixed w-full h-full top-0 left-0 flex items-center justify-center">
			<div className="modal-overlay absolute w-full h-full bg-gray-900 opacity-70"></div>

			<div
				className="modal-container bg-white w-11/12 md:max-w-md mx-auto rounded shadow-lg z-50 overflow-y-auto"
				style={{ width: '600px' }}
			>
				<div className="modal-content py-4 text-left px-6">
					<div className="p-3">
						<div className="flex justify-center py-2">
							<div className="loader"></div>
						</div>
						<div className="text-xl text-center font-bold">Please wait...</div>
						<div className="text-xl text-center font-bold">
							Your website is being created 🖌️
						</div>
						<div className="py-3">
							Normally, it takes around 2-3 minutes. This is because, we are
							sending the complete 15-20 mb file at once.
						</div>
						<div className="text-blue-500">
							We will soon be adding a feature to send the file in chunks, to reduce the time by 90%.
						</div>
					</div>
				</div>
			</div>
		</div>
	);
}

export default MyLoadingModal;
