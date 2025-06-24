"use client"

import { useState, useCallback } from "react"
import { useDropzone } from "react-dropzone"
import { Upload, X, FileText, CheckCircle } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Progress } from "@/components/ui/progress"

interface FileUploadProps {
    onClose: () => void
}

interface UploadFile {
    file: File
    progress: number
    status: "uploading" | "processing" | "complete" | "error"
    id: string
}

export function FileUpload({ onClose }: FileUploadProps) {
    const [uploadFiles, setUploadFiles] = useState<UploadFile[]>([])

    const onDrop = useCallback((acceptedFiles: File[]) => {
        const newFiles = acceptedFiles.map((file) => ({
            file,
            progress: 0,
            status: "uploading" as const,
            id: Math.random().toString(36).substr(2, 9),
        }))

        setUploadFiles((prev) => [...prev, ...newFiles])

        // Simulate upload progress
        newFiles.forEach((uploadFile) => {
            simulateUpload(uploadFile.id)
        })
    }, [])

    const simulateUpload = (fileId: string) => {
        const interval = setInterval(() => {
            setUploadFiles((prev) =>
                prev.map((file) => {
                    if (file.id === fileId) {
                        if (file.progress < 100) {
                            return { ...file, progress: file.progress + 10 }
                        } else if (file.status === "uploading") {
                            return { ...file, status: "processing" }
                        } else if (file.status === "processing") {
                            clearInterval(interval)
                            return { ...file, status: "complete" }
                        }
                    }
                    return file
                }),
            )
        }, 200)
    }

    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop,
        accept: {
            "application/pdf": [".pdf"],
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document": [".docx"],
            "text/plain": [".txt"],
        },
        multiple: true,
    })

    const removeFile = (fileId: string) => {
        setUploadFiles((prev) => prev.filter((file) => file.id !== fileId))
    }

    return (
        <div className="space-y-6">
            <div
                {...getRootProps()}
                className={`border-2 border-dashed rounded-lg p-8 text-center cursor-pointer transition-colors ${
                    isDragActive ? "border-blue-400 bg-blue-50" : "border-gray-300 hover:border-gray-400"
                }`}
            >
                <input {...getInputProps()} />
                <Upload className="mx-auto h-12 w-12 text-gray-400 mb-4" />
                {isDragActive ? (
                    <p className="text-blue-600">Drop the files here...</p>
                ) : (
                    <div>
                        <p className="text-gray-600 mb-2">Drag and drop files here, or click to select files</p>
                        <p className="text-sm text-gray-500">Supports PDF, DOCX, and TXT files up to 10MB</p>
                    </div>
                )}
            </div>

            {uploadFiles.length > 0 && (
                <div className="space-y-3">
                    <h4 className="font-medium text-gray-900">Uploading Files</h4>
                    {uploadFiles.map((uploadFile) => (
                        <div key={uploadFile.id} className="flex items-center space-x-3 p-3 bg-gray-50 rounded-lg">
                            <FileText className="h-8 w-8 text-gray-400 flex-shrink-0" />
                            <div className="flex-1 min-w-0">
                                <p className="text-sm font-medium text-gray-900 truncate">{uploadFile.file.name}</p>
                                <div className="flex items-center space-x-2 mt-1">
                                    {uploadFile.status === "uploading" && (
                                        <>
                                            <Progress value={uploadFile.progress} className="flex-1 h-2" />
                                            <span className="text-xs text-gray-500">{uploadFile.progress}%</span>
                                        </>
                                    )}
                                    {uploadFile.status === "processing" && <span className="text-xs text-yellow-600">Processing...</span>}
                                    {uploadFile.status === "complete" && (
                                        <div className="flex items-center space-x-1">
                                            <CheckCircle className="h-4 w-4 text-green-500" />
                                            <span className="text-xs text-green-600">Complete</span>
                                        </div>
                                    )}
                                </div>
                            </div>
                            <Button variant="ghost" size="sm" onClick={() => removeFile(uploadFile.id)} className="flex-shrink-0">
                                <X className="h-4 w-4" />
                            </Button>
                        </div>
                    ))}
                </div>
            )}

            <div className="flex justify-end space-x-3">
                <Button variant="outline" onClick={onClose}>
                    Cancel
                </Button>
                <Button disabled={uploadFiles.length === 0}>Generate Study Materials</Button>
            </div>
        </div>
    )
}
