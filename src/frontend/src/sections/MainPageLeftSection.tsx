import React from 'react';

interface Props {
   onChange: (e: boolean) => void;
   selectedCard: React.ComponentType;
   onSelect: () => void;
}

export default function LeftSection({ }: Props) {
   return <div style={{ marginTop: '200px' }}>{/*<Searching />*/}</div>;
}
