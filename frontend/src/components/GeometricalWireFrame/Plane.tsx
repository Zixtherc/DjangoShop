import React, { useRef, useMemo } from 'react'
import { Canvas, useFrame } from '@react-three/fiber'
import * as THREE from 'three'
import { Wireframe } from 'three/examples/jsm/Addons.js';

const WavePlane= () => {
  const meshRef = useRef<any>(null);

  const rows = 40;
  const columns = 40;

  useFrame(({clock}) => {
    const time = clock.getElapsedTime()
    const {geometry} = meshRef.current;
    const pos = geometry.attributes.position;


  })
  return(
    <mesh ref={meshRef} rotation={[-Math.PI / 2, 0 ,0]}>
      <planeGeometry args={[15,10,rows,columns]}/>
      <meshBasicMaterial color='#ffffff' wireframe/>

    </mesh>
  )
}

export default function GravityGrid(){
  return (
    <div style={{ width: '100vw', height: '100vh' }}>
      <Canvas
        camera={{ position: [0, 5, 10], fov: 60, far: 500, near: 0.1 }}
        gl={{
          alpha: false,
          antialias: true,
        }}>
        <color attach="background" args={['#000']} />
        <WavePlane />
      </Canvas>
    </div>
  )
}