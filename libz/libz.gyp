{
	'includes':
	[
		'../../common.gypi',
	],
	
	'conditions':
	[
		[
			'use_system_libz == 0',
			{
				'targets':
				[
					{
						'target_name': 'libz',
						'type': 'static_library',
						
						'variables':
						{
							'library_for_module': 1,
						},
						
						'include_dirs':
						[
							'include',
							'src',
						],
						
						'sources':
						[
							'include/zconf.h',
							'include/zlib.h',
							
							'src/crc32.h',
							'src/deflate.h',
							'src/inffast.h',
							'src/inffixed.h',
							'src/inflate.h',
							'src/inftrees.h',
							'src/trees.h',
							'src/zutil.h',
							
							'src/adler32.c',
							'src/compress.c',
							'src/crc32.c',
							'src/deflate.c',
							'src/gzio.c',
							'src/infback.c',
							'src/inffast.c',
							'src/inflate.c',
							'src/inftrees.c',
							'src/trees.c',
							'src/uncompr.c',
							'src/zutil.c',
						],
						
						'direct_dependent_settings':
						{
							'include_dirs':
							[
								'include',
							],
						},
					},
				],
			},
			{
				'targets':
				[
					{
						'target_name': 'libz',
						'type': 'none',
						
						'link_settings':
						{
							'libraries':
							[
								'-lz',
							],
						},
					},
				],
			},
		],
	],
}