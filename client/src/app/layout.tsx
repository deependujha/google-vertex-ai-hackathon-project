import './globals.css';
import type { Metadata } from 'next';
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
	title: '2 min Online',
	description:
		'`2 min online` is the easiest way to create a website for your business. It was created in a hackathon by a team of 3 people from 3 different countries (US, India, and Pakistan).',
};

export default function RootLayout({
	children,
}: {
	children: React.ReactNode;
}) {
	return (
		<html lang="en">
			<body className={inter.className}>{children}</body>
		</html>
	);
}
