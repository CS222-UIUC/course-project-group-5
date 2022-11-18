export type ReviewType = {
   apt_id: number;
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
   votes: number;
};
