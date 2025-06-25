"use client"

import { useState } from "react"
import { Upload, FileText, Brain, Clock, TrendingUp } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import {FileUpload} from "@/components/file-upload";


const recentUploads = [
    { id: 1, name: "Biology Chapter 12.pdf", date: "2024-01-15", status: "processed" },
    { id: 2, name: "History Notes.docx", date: "2024-01-14", status: "processing" },
    { id: 3, name: "Chemistry Formulas.txt", date: "2024-01-13", status: "processed" },
    { id: 4, name: "Math Equations.pdf", date: "2024-01-12", status: "processed" },
]

const stats = [
    { label: "Files Uploaded", value: "24", icon: FileText, color: "text-blue-600" },
    { label: "Flashcards Generated", value: "342", icon: Brain, color: "text-green-600" },
    { label: "Study Sessions", value: "18", icon: Clock, color: "text-purple-600" },
    { label: "Success Rate", value: "87%", icon: TrendingUp, color: "text-orange-600" },
]

export default function Dashboard() {
    const [showUpload, setShowUpload] = useState(false)

    return (
        <div className="p-8">
            <div className="max-w-7xl mx-auto">
                {/* Header */}
                <div className="mb-8">
                    <h1 className="text-3xl font-bold text-gray-900 mb-2">Welcome back! 👋</h1>
                    <p className="text-gray-600">Ready to boost your learning? Upload new materials or continue studying.</p>
                </div>

                {/* Stats Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
                    {stats.map((stat) => (
                        <Card key={stat.label}>
                            <CardContent className="p-6">
                                <div className="flex items-center justify-between">
                                    <div>
                                        <p className="text-sm font-medium text-gray-600 mb-1">{stat.label}</p>
                                        <p className="text-2xl font-bold text-gray-900">{stat.value}</p>
                                    </div>
                                    <div className={`p-3 rounded-full bg-gray-50 ${stat.color}`}>
                                        <stat.icon className="h-6 w-6" />
                                    </div>
                                </div>
                            </CardContent>
                        </Card>
                    ))}
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
                    {/* Upload Section */}
                    <div className="lg:col-span-2">
                        <Card>
                            <CardHeader>
                                <CardTitle className="flex items-center space-x-2">
                                    <Upload className="h-5 w-5" />
                                    <span>Upload Study Materials</span>
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                {!showUpload ? (
                                    <div className="text-center py-12">
                                        <div className="mx-auto h-16 w-16 bg-blue-50 rounded-full flex items-center justify-center mb-4">
                                            <Upload className="h-8 w-8 text-blue-600" />
                                        </div>
                                        <h3 className="text-lg font-medium text-gray-900 mb-2">Upload your study materials</h3>
                                        <p className="text-gray-600 mb-6">
                                            Drag and drop files or click to browse. We support PDF, DOCX, and TXT files.
                                        </p>
                                        <Button onClick={() => setShowUpload(true)}>Choose Files</Button>
                                    </div>
                                ) : (
                                    <FileUpload onClose={() => setShowUpload(false)} />
                                )}
                            </CardContent>
                        </Card>
                    </div>

                    {/* Recent Uploads */}
                    <div>
                        <Card>
                            <CardHeader>
                                <CardTitle>Recent Uploads</CardTitle>
                            </CardHeader>
                            <CardContent className="space-y-4">
                                {recentUploads.map((upload) => (
                                    <div key={upload.id} className="flex items-center space-x-3">
                                        <div className="flex-shrink-0">
                                            <FileText className="h-8 w-8 text-gray-400" />
                                        </div>
                                        <div className="flex-1 min-w-0">
                                            <p className="text-sm font-medium text-gray-900 truncate">{upload.name}</p>
                                            <p className="text-xs text-gray-500">{upload.date}</p>
                                        </div>
                                        <div className="flex-shrink-0">
                                            {upload.status === "processing" ? (
                                                <div className="flex items-center space-x-2">
                                                    <div className="h-2 w-2 bg-yellow-400 rounded-full animate-pulse"></div>
                                                    <span className="text-xs text-yellow-600">Processing</span>
                                                </div>
                                            ) : (
                                                <div className="flex items-center space-x-2">
                                                    <div className="h-2 w-2 bg-green-400 rounded-full"></div>
                                                    <span className="text-xs text-green-600">Ready</span>
                                                </div>
                                            )}
                                        </div>
                                    </div>
                                ))}
                            </CardContent>
                        </Card>
                    </div>
                </div>
            </div>
        </div>
    )
}
