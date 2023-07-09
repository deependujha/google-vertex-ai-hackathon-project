import Swal from 'sweetalert2';

const successAlert = () => {
	Swal.fire({
		icon: 'success',
		title: 'Done!',
		text: 'Your request has been completed!',
		showConfirmButton: false,
		timer: 1500,
	});
};

const errorAlert = () => {
	Swal.fire({
		icon: 'error',
		title: 'Oops...',
		text: 'Something went wrong!',
		showConfirmButton: false,
		timer: 3000,
	});
};

export { successAlert, errorAlert };
