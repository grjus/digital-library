export type AuthorDto = {
  id: string;
  fullname: string;
  email: string;
  age: string;
};

type AuthorDetailsDto = {
  bio?: string;
  awards?: string[];
  photo_url?: string;
  published_books?: string[];
  nationality?: string;
  website?: string;
  social_media_links?: Record<string, string>;
};

export type AuthorDtoWithDetails = AuthorDto & {
  author_details: AuthorDetailsDto | null;
};
