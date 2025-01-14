"""Factory module for creating storage backends."""

import os
import logging
from typing import Optional
from pathlib import Path
from storage import StorageBackend
from storage.git_storage import GitStorage
from storage.sqlite_storage import SQLiteStorage

logger = logging.getLogger(__name__)

def create_storage(storage_type: str = 'sqlite', **kwargs) -> StorageBackend:
    """Create a storage backend based on configuration.
    
    Args:
        storage_type: Type of storage backend ('git' or 'sqlite')
        **kwargs: Additional configuration parameters
    
    Returns:
        StorageBackend instance
    
    Raises:
        ValueError: If storage_type is invalid
    """
    try:
        logger.info(f"Creating storage backend of type: {storage_type}")
        logger.debug(f"Storage configuration: {kwargs}")
        
        # Use environment variable if storage_type not specified
        if storage_type is None:
            storage_type = os.getenv('MARBELLACHAT_STORAGE', 'sqlite').lower()
            logger.info(f"Using storage type from environment: {storage_type}")
        
        storage_type = storage_type.lower()
        
        if storage_type == 'git':
            logger.debug("Initializing Git storage backend")
            return GitStorage(**kwargs)
        elif storage_type == 'sqlite':
            logger.debug("Initializing SQLite storage backend")
            return SQLiteStorage(**kwargs)
        else:
            error_msg = f"Invalid storage type: {storage_type}"
            logger.error(error_msg)
            raise ValueError(error_msg)
            
    except Exception as e:
        logger.error(f"Error creating storage backend", exc_info=True)
        raise
