import React from 'react';
import Searching from '../components/SearchAndDisplayResults';

interface Props {
   onChange: (e: boolean) => void;
   selectedCard: React.ComponentType;
   onSelect: () => void;
}

export default function LeftSection({ onChange }: Props) {
   return <div style={{ marginTop: '200px' }}>{/*<Searching />*/}</div>;
}
