export default function Button({ children, ...props }) {
  return (
    <button
      {...props}
      className='bg-amber-400 text-stone-900 py-2 px-4 rounded-lg shadow-md hover:bg-amber-600'
    >
      {children}
    </button>
  );
}