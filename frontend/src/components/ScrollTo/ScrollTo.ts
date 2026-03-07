import { useRef } from "react";
import type { MouseEvent } from "react"; 

export const useSmoothScroll = () => {
  const elementRef = useRef<HTMLDivElement>(null);

  const scrollToElement = (e?: MouseEvent) => {
    if (e) e.preventDefault();
    
    elementRef.current?.scrollIntoView({
      behavior: "smooth",
      block: "start",
    });
  };

  return [elementRef, scrollToElement] as const;
};