import Link from "next/link";

interface BreadcrumbItem {
  label: string;
  href?: string;
}

interface BreadcrumbProps {
  items: BreadcrumbItem[];
}

export function Breadcrumb({ items }: BreadcrumbProps) {
  return (
    <nav className="mb-4 flex items-center gap-1.5 text-xs">
      <Link href="/" className="opacity-40 hover:opacity-70">
        Home
      </Link>
      {items.map((item, i) => (
        <span key={i} className="flex items-center gap-1.5">
          <span className="opacity-20">/</span>
          {item.href ? (
            <Link href={item.href} className="opacity-40 hover:opacity-70">
              {item.label}
            </Link>
          ) : (
            <span className="opacity-60">{item.label}</span>
          )}
        </span>
      ))}
    </nav>
  );
}
