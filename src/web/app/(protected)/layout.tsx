import { redirect } from 'next/navigation'
import { Sidebar } from "@/components/sidebar";
import { auth0 } from "@/lib/auth0";
import { ReactNode } from 'react'

interface ProtectedLayoutProps {
    children: ReactNode
}

export default async function ProtectedLayout({ children }: ProtectedLayoutProps) {
    const session = await auth0.getSession();

    // Redirect to login if not authenticated
    if (!session) {
        redirect('/api/auth/login')
    }

    return (
        <div className="flex h-screen bg-gray-100">
            <Sidebar />
            <main className="flex-1 overflow-auto">
                {children}
            </main>
        </div>
    )
}