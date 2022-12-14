export type ReviewType = {
   id: number;
   username: string;
   date: string;
   comment: string;
   vote: boolean;
};

export type PicType = {
   url: string;
};

export type AptType = {
   id: number;
   name: string;
   address: string;
   price_min: number;
   price_max: number;
   rating: number;
};

export type UserType = {
   user_id: number;
   username: string;
   password: string;
   email: string;
   phone: string;
};
