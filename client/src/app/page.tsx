import Image from 'next/image';
import MyFooter from '../components/MyFooter';
import MyForm from '../components/MyForm';
import LandingPageComponent from '../components/LandingPageComponent';

export default function Home() {
	return (
		<>
			<LandingPageComponent />
			<MyForm />
			<MyFooter />
		</>
	);
}
