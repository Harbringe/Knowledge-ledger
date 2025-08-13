import os
from django.utils import timezone
from django.utils.text import slugify

def course_image_upload_path(instance, filename):
    """
    Generate compact upload path for course images: c/cid/img.ext
    Target: < 64 bytes
    """
    if hasattr(instance, 'course_id'):
        course_id = instance.course_id
    elif hasattr(instance, 'course') and instance.course:
        course_id = instance.course.course_id
    else:
        course_id = 'u'  # unknown
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create compact filename: cid-img.ext
    new_filename = f"{course_id}-img{ext}"
    
    return f"c/{course_id}/{new_filename}"

def course_video_upload_path(instance, filename):
    """
    Generate compact upload path for course videos: c/cid/vid.ext
    Target: < 64 bytes
    """
    if hasattr(instance, 'course_id'):
        course_id = instance.course_id
    elif hasattr(instance, 'course') and instance.course:
        course_id = instance.course.course_id
    elif hasattr(instance, 'variant') and instance.variant and instance.variant.course:
        course_id = instance.variant.course.course_id
    else:
        course_id = 'u'  # unknown
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create compact filename: cid-vid.ext
    new_filename = f"{course_id}-vid{ext}"
    
    return f"c/{course_id}/{new_filename}"

def course_file_upload_path(instance, filename):
    """
    Generate compact upload path for course files: c/cid/doc.ext
    Target: < 64 bytes
    """
    if hasattr(instance, 'course_id'):
        course_id = instance.course_id
    elif hasattr(instance, 'course') and instance.course:
        course_id = instance.course.course_id
    elif hasattr(instance, 'variant') and instance.variant and instance.variant.course:
        course_id = instance.variant.course.course_id
    else:
        course_id = 'u'  # unknown
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create compact filename: cid-doc.ext
    new_filename = f"{course_id}-doc{ext}"
    
    return f"c/{course_id}/{new_filename}"

def teacher_image_upload_path(instance, filename):
    """
    Generate compact upload path for teacher images: t/tid/img.ext
    Target: < 64 bytes
    """
    if hasattr(instance, 'user') and instance.user:
        teacher_id = instance.user.id
    else:
        teacher_id = 'u'  # unknown
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create compact filename: tid-img.ext
    new_filename = f"{teacher_id}-img{ext}"
    
    return f"t/{teacher_id}/{new_filename}"

def category_image_upload_path(instance, filename):
    """
    Generate compact upload path for category images: cat/cid/img.ext
    Target: < 64 bytes
    """
    if hasattr(instance, 'id'):
        category_id = instance.id
    else:
        category_id = 'u'  # unknown
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create compact filename: cid-img.ext
    new_filename = f"{category_id}-img{ext}"
    
    return f"cat/{category_id}/{new_filename}"

def user_avatar_upload_path(instance, filename):
    """
    Generate compact upload path for user avatars: u/uid/av.ext
    Target: < 64 bytes
    """
    if hasattr(instance, 'id'):
        user_id = instance.id
    else:
        user_id = 'u'  # unknown
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create compact filename: uid-av.ext
    new_filename = f"{user_id}-av{ext}"
    
    return f"u/{user_id}/{new_filename}"

def certificate_pdf_upload_path(instance, filename):
    """
    Generate compact upload path for certificates: cert/cid-uid.pdf
    Target: < 64 bytes
    """
    if hasattr(instance, 'course') and instance.course:
        course_id = instance.course.course_id
    else:
        course_id = 'u'  # unknown
    
    if hasattr(instance, 'user') and instance.user:
        user_id = instance.user.id
    else:
        user_id = 'u'  # unknown
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create compact filename: cid-uid.pdf
    new_filename = f"{course_id}-{user_id}{ext}"
    
    return f"cert/{new_filename}"

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

def get_compact_filename(instance, filename, prefix=''):
    """
    Generate ultra-compact filename for any file type
    Target: < 64 bytes total URL length
    """
    # Get instance ID (course_id, user_id, etc.)
    instance_id = None
    if hasattr(instance, 'course_id'):
        instance_id = instance.course_id
    elif hasattr(instance, 'id'):
        instance_id = instance.id
    elif hasattr(instance, 'user') and instance.user:
        instance_id = instance.user.id
    else:
        instance_id = 'u'
    
    # Get file extension
    ext = os.path.splitext(filename)[1]
    
    # Create ultra-compact filename: prefix-id.ext
    if prefix:
        new_filename = f"{prefix}-{instance_id}{ext}"
    else:
        new_filename = f"{instance_id}{ext}"
    
    return new_filename

def get_upload_path_info():
    """
    Return information about the compact naming system
    """
    return {
        "naming_convention": "Compact URLs under 64 bytes",
        "prefixes": {
            "c": "course files",
            "t": "teacher files", 
            "cat": "category files",
            "u": "user files",
            "cert": "certificates"
        },
        "examples": {
            "course_image": "c/ABC123/ABC123-img.jpg",
            "course_video": "c/ABC123/ABC123-vid.mp4",
            "teacher_image": "t/456/456-img.jpg",
            "user_avatar": "u/789/789-av.png",
            "certificate": "cert/ABC123-789.pdf"
        },
        "url_lengths": {
            "base_cloudinary": "https://res.cloudinary.com/cloudname/image/upload/",
            "course_image": "c/ABC123/ABC123-img.jpg",
            "total_example": "https://res.cloudinary.com/cloudname/image/upload/c/ABC123/ABC123-img.jpg"
        }
    }
