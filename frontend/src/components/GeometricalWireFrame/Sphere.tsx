import { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';

function WireFrameSphere() {
  const meshRef = useRef<any>(null);

  useFrame((_state: any, delta) => {
    if (meshRef.current) {
      meshRef.current.rotation.y += delta * 0.05; 
    }
  });

  return (
    <mesh ref={meshRef}>
      <icosahedronGeometry args={[2.3, 3]} />
      <meshBasicMaterial color="#ffffff" wireframe transparent opacity={0.05} />
    </mesh>
  );
}

export default function SphereScene({ className }: any) {
    return (
        <div className={className} style={{ width: '100%', height: '100%' }}>
            <Canvas camera={{ position: [0, 0, 5] }}>
                <WireFrameSphere />
            </Canvas>
        </div>
    );
}