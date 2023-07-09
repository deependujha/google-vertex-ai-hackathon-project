import React from 'react';
import Image from 'next/image';
import { Fasthand } from 'next/font/google';

const fasthand = Fasthand({ weight: '400', subsets: ['latin'] });

const LandingPageComponent = () => {
	return (
		<div
			className="bg-gradient-to-r from-indigo-500 flex justify-around items-center "
			style={{ height: '100vh' }}
		>
			<div>
				<div
					className={`text-3xl ${fasthand.className} py-3`}
					style={{ fontSize: '50px' }}
				>
					Make your online presence
				</div>
				<div
					className={`text-3xl py-3 ${fasthand.className}`}
					style={{ fontSize: '50px' }}
				>
					in 2 minutes...
				</div>
			</div>
			<Image
				className="rounded-3xl"
				src="/websiteMaking.png"
				width={500}
				height={500}
				alt="websiteMaking"
			/>
		</div>
	);
};

export default LandingPageComponent;
