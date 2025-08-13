import os
from django.utils import timezone
from django.utils.text import slugify

def course_image_upload_path(instance, filename):
    """
    Generate upload path for course images: course-file/courseid-img/filename
    """
    if hasattr(instance, 'course_id'):
        course_id = instance.course_id
    elif hasattr(instance, 'course') and instance.course:
        course_id = instance.course.course_id
    else:
        course_id = 'unknown'
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create descriptive filename
    new_filename = f"{course_id}-img{ext}"
    
    return f"course-file/{course_id}-img/{new_filename}"

def course_video_upload_path(instance, filename):
    """
    Generate upload path for course videos: course-file/courseid-video/filename
    """
    if hasattr(instance, 'course_id'):
        course_id = instance.course_id
    elif hasattr(instance, 'course') and instance.course:
        course_id = instance.course.course_id
    elif hasattr(instance, 'variant') and instance.variant and instance.variant.course:
        course_id = instance.variant.course.course_id
    else:
        course_id = 'unknown'
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create descriptive filename
    new_filename = f"{course_id}-video{ext}"
    
    return f"course-file/{course_id}-video/{new_filename}"

def course_file_upload_path(instance, filename):
    """
    Generate upload path for course files: course-file/courseid-file/filename
    """
    if hasattr(instance, 'course_id'):
        course_id = instance.course_id
    elif hasattr(instance, 'course') and instance.course:
        course_id = instance.course.course_id
    elif hasattr(instance, 'variant') and instance.variant and instance.variant.course:
        course_id = instance.variant.course.course_id
    else:
        course_id = 'unknown'
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create descriptive filename
    new_filename = f"{course_id}-file{ext}"
    
    return f"course-file/{course_id}-file/{new_filename}"

def teacher_image_upload_path(instance, filename):
    """
    Generate upload path for teacher images: course-file/teacher-teacherid-img/filename
    """
    if hasattr(instance, 'user') and instance.user:
        teacher_id = instance.user.id
    else:
        teacher_id = 'unknown'
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create descriptive filename
    new_filename = f"teacher-{teacher_id}-img{ext}"
    
    return f"course-file/teacher-{teacher_id}-img/{new_filename}"

def category_image_upload_path(instance, filename):
    """
    Generate upload path for category images: course-file/category-categoryid-img/filename
    """
    if hasattr(instance, 'id'):
        category_id = instance.id
    else:
        category_id = 'unknown'
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create descriptive filename
    new_filename = f"category-{category_id}-img{ext}"
    
    return f"course-file/category-{category_id}-img/{new_filename}"

def user_avatar_upload_path(instance, filename):
    """
    Generate upload path for user avatars: user_folder/user-userid-avatar/filename
    """
    if hasattr(instance, 'id'):
        user_id = instance.id
    else:
        user_id = 'unknown'
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create descriptive filename
    new_filename = f"user-{user_id}-avatar{ext}"
    
    return f"user_folder/user-{user_id}-avatar/{new_filename}"

def certificate_pdf_upload_path(instance, filename):
    """
    Generate upload path for certificates: certificates/courseid-userid-certificate.pdf
    """
    if hasattr(instance, 'course') and instance.course:
        course_id = instance.course.course_id
    else:
        course_id = 'unknown'
    
    if hasattr(instance, 'user') and instance.user:
        user_id = instance.user.id
    else:
        user_id = 'unknown'
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create descriptive filename
    new_filename = f"{course_id}-{user_id}-certificate{ext}"
    
    return f"certificates/{new_filename}"

def get_file_type(filename):
    """
    Determine if a file is an image, video, or other file type
    """
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg'}
    video_extensions = {'.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mkv', '.m4v'}
    
    ext = os.path.splitext(filename)[1].lower()
    
    if ext in image_extensions:
        return 'image'
    elif ext in video_extensions:
        return 'video'
    else:
        return 'file'
