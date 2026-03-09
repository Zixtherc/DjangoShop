import { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';

function WireFrameSphere() {
  const meshRef = useRef<any>(null);

  useFrame((state: any) => {
    if (meshRef.current) {

      meshRef.current.rotation.y %= Math.PI * 2;
      meshRef.current.rotation.x %= Math.PI * 2;

      const mouseImpactY = state.mouse.x * 0.3;
      const mouseImpactX = state.mouse.y * 0.3;

      meshRef.current.rotation.x += (mouseImpactY * 0.01);
      meshRef.current.rotation.y += (mouseImpactX * 0.01);
    }
  });

  return (
    <mesh ref={meshRef}>
      <icosahedronGeometry args={[2.3, 4]} />
      <meshBasicMaterial color="#ffffff" wireframe transparent opacity={0.05} />
    </mesh>
  );
}

export default function SphereScene({ className }: any) {
    return (
        <div className={className} style={{ width: '100%', height: '100%' }}>
            <Canvas eventSource={document.getElementById('root') || undefined} camera={{ position: [0, 0, 5] }}>
                <WireFrameSphere />
            </Canvas>
        </div>
    );
}