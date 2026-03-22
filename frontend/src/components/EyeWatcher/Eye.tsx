import React, { useState, useEffect, useRef } from 'react';

const Eye: React.FC = () => {
  const [angle, setAngle] = useState(0);
  const [isClosed, setIsClosed] = useState(false);
  const eyeRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (eyeRef.current && !isClosed) {
        const rect = eyeRef.current.getBoundingClientRect();
        const eyeX = rect.left + rect.width / 2;
        const eyeY = rect.top + rect.height / 2;

        const radian = Math.atan2(e.clientY - eyeY, e.clientX - eyeX);
        const rotation = (radian * 180) / Math.PI;
        setAngle(rotation);
      }
    };

    window.addEventListener('mousemove', handleMouseMove);
    return () => window.removeEventListener('mousemove', handleMouseMove);
  }, [isClosed]);
  return(
    <div>
        
    </div>
  )
};

export default Eye;