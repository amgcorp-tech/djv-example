import axios, {
    AxiosRequest,
    AxiosResponse,
    AxiosError
} from 'axios';


export const djangoVite = axios.create({
  baseURL: import.meta.env.VITE_BACKEND_URL,
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFTOKEN',
  withCredentials: true
});

djangoVite.interceptors.request.use((request: AxiosRequest) => {
  return request;
});

djangoVite.interceptors.response.use(
  (response: AxiosResponse) => response,
  (error: AxiosError) => {
    if (
      error.response?.status === 403 &&
      error.response?.data?.message === 'You are not permitted to perform this action.'
    ) {
      return;
    }
    throw error;
  }
);
