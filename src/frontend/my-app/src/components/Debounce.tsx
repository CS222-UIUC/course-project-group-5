import React, { useEffect, useState } from "react";

// spaces out user entry and function execution to not overload the server
export const Debounce = (value: any, delay: any) => {
    const [debouncedValue, setDebouncedValue] = useState(value);

    useEffect(() => {
        const timer = setTimeout(() => setDebouncedValue(value), delay);

        return () => {
            clearTimeout(timer);
        };
    }, [value, delay]);
    return debouncedValue;
};
