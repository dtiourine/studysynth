"use client"

import Link from "next/link"
import { usePathname } from "next/navigation"
import { Home, BookOpen, Brain } from "lucide-react"
import { cn } from "@/lib/utils"

const navigation = [
    { name: "Dashboard", href: "/", icon: Home },
    { name: "Study Materials", href: "/materials", icon: BookOpen },
    { name: "Study Session", href: "/study", icon: Brain },
]

export function Sidebar() {
    const pathname = usePathname()

    return (
        <div className="flex h-screen w-64 flex-col bg-white border-r border-gray-200">
            <div className="flex h-16 items-center px-6 border-b border-gray-200">
                <div className="flex items-center space-x-2">
                    <div className="h-8 w-8 bg-blue-600 rounded-lg flex items-center justify-center">
                        <Brain className="h-5 w-5 text-white" />
                    </div>
                    <span className="text-xl font-bold text-gray-900">StudySynth</span>
                </div>
            </div>

            <nav className="flex-1 px-4 py-6 space-y-2">
                {navigation.map((item) => {
                    const isActive = pathname === item.href
                    return (
                        <Link
                            key={item.name}
                            href={item.href}
                            className={cn(
                                "flex items-center px-3 py-2 text-sm font-medium rounded-lg transition-colors",
                                isActive
                                    ? "bg-blue-50 text-blue-700 border border-blue-200"
                                    : "text-gray-600 hover:bg-gray-50 hover:text-gray-900",
                            )}
                        >
                            <item.icon className="mr-3 h-5 w-5" />
                            {item.name}
                        </Link>
                    )
                })}
            </nav>

            <div className="p-4 border-t border-gray-200">
                <div className="flex items-center space-x-3">
                    <div className="h-8 w-8 bg-gray-300 rounded-full flex items-center justify-center">
                        <span className="text-sm font-medium text-gray-700">JD</span>
                    </div>
                    <div>
                        <p className="text-sm font-medium text-gray-900">John Doe</p>
                        <p className="text-xs text-gray-500">john@example.com</p>
                    </div>
                </div>
            </div>
        </div>
    )
}
