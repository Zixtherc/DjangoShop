import type { ReactNode } from 'react'; 
import Navbar from '../components/Navbar/Navbar';

interface LayoutProps {
  children: ReactNode;
}

export default function Layout({ children }: LayoutProps) {
  return (
    <div>
      <div className="monolith-box">
        <Navbar />
        <main className="content-area">
          {children}
        </main>
      </div>
    </div>
  );
}